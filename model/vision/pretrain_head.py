import torch
import torch.nn as nn
import torch.nn.functional as F
from pipeline.registry import registry
from model.vision.basic_modules import get_mlp_head

class BertPredictionHeadTransform(nn.Module):
    def __init__(self, hidden_size, hidden_act='gelu'):
        super().__init__()
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.transform_act_fn = F.gelu
        self.LayerNorm = nn.LayerNorm(hidden_size)

    def forward(self, hidden_states):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.transform_act_fn(hidden_states)
        hidden_states = self.LayerNorm(hidden_states)
        return hidden_states

class BertLMPredictionHead(nn.Module):
    def __init__(self, hidden_size, vocab_size):
        super().__init__()
        self.transform = BertPredictionHeadTransform(hidden_size=hidden_size, hidden_act='gelu')

        self.decoder = nn.Linear(hidden_size, vocab_size, bias=False)

        self.bias = nn.Parameter(torch.zeros(vocab_size))

    def forward(self, hidden_states):
        hidden_states = self.transform(hidden_states)
        hidden_states = self.decoder(hidden_states) + self.bias
        return hidden_states

@registry.register_other_model("pretrain_head_v1")
class PretrainHeadV1(nn.Module):
    def __init__(self, hidden_size=768, vocab_size=30522):
        super().__init__()
        self.lm_pred_head = BertLMPredictionHead(hidden_size, vocab_size)
        self.contrastive_head = get_mlp_head(hidden_size, hidden_size, 2)
        
    def forward(self, txt_embeds):
        txt_lm_cls_logits = self.lm_pred_head(txt_embeds)
        scene_txt_match_logit = self.contrastive_head(txt_embeds[:, 0, :])
        return txt_lm_cls_logits, scene_txt_match_logit