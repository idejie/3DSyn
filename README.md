# 3D Vision and Language Pretraining with Large-Scale Synthetic Data

### Install
1. Install conda package
```
conda env create --name 3dsyn --file=environments.yml
```

2. install pointnet2
```
cd vision/pointnet2
python3 setup.py install
```
### Prepare dataset
1. Follow [Vil3dref](https://github.com/cshizhe/vil3dref) and download scannet data under `data/scanfamily/scan_data`, this folder should look like
```
./data/scanfamily/scan_data/
├── instance_id_to_gmm_color
├── instance_id_to_loc
├── instance_id_to_name
└── pcd_with_global_alignment
```
2. Download [scanrefer+referit3d](https://github.com/cshizhe/vil3dref), [scanqa](https://github.com/ATR-DBI/ScanQA), and [sqa3d](https://github.com/SilongYong/SQA3D), and put them under `/data/scanfamily/annotations`

```
data/scanfamily/annotations/
├── meta_data
│   ├── cat2glove42b.json
│   ├── scannetv2-labels.combined.tsv
│   ├── scannetv2_raw_categories.json
│   ├── scanrefer_corpus.pth
│   └── scanrefer_vocab.pth
├── qa
│   ├── ScanQA_v1.0_test_w_obj.json
│   ├── ScanQA_v1.0_test_wo_obj.json
│   ├── ScanQA_v1.0_train.json
│   └── ScanQA_v1.0_val.json
├── refer
│   ├── nr3d.jsonl
│   ├── scanrefer.jsonl
│   ├── sr3d+.jsonl
│   └── sr3d.jsonl
├── splits
│   ├── scannetv2_test.txt
│   ├── scannetv2_train.txt
│   └── scannetv2_val.txt
└── sqa_task
    ├── answer_dict.json
    └── balanced
        ├── v1_balanced_questions_test_scannetv2.json
        ├── v1_balanced_questions_train_scannetv2.json
        ├── v1_balanced_questions_val_scannetv2.json
        ├── v1_balanced_sqa_annotations_test_scannetv2.json
        ├── v1_balanced_sqa_annotations_train_scannetv2.json
        └── v1_balanced_sqa_annotations_val_scannetv2.json
```


### Evaluation
Download all checkpoints and put them under `project/pretrain_weights`

| Checkpoint           | Link                                                         | Note                                              |
| :------------------- | ------------------------------------------------------------ | ------------------------------------------------- |
| Pretrain | [link](https://pan.baidu.com/s/1oyW4ZqmmJn-sp3vDLCaPYQ?pwd=45pu)||
| ScanRefer            | [link](https://pan.baidu.com/s/13JGq-nA0llWHZ0k0lySufw?pwd=agrk) | Fine-tuned ScanRefer from pre-trained checkpoint. |
| ScanQA               | [link](https://pan.baidu.com/s/123CkrlA67pBr295CGHFbsQ?pwd=r76v) | Fine-tined ScanQA from pre-trained checkpoint.    |
| Sr3D                 | [link](https://pan.baidu.com/s/123CkrlA67pBr295CGHFbsQ?pwd=r76v) | Fine-tuned Sr3D from pre-trained checkpoint.      |
| Nr3D                 | [link](https://pan.baidu.com/s/1g2fWLBFi0_c9Gt9EwgMnTQ?pwd=mrjs) | Fine-tuned Nr3D from pre-trained checkpoint.      |
| Scan2Cap             | [link](https://pan.baidu.com/s/1TTfboFXRV86yb2u5frkUKg?pwd=xurm) | Fine-tuned Scan2Cap from pre-trained checkpoint.  |

#### Run 
To run the model, use the following command, task includes scanrefer, scanqa, sr3d, nr3d, and scan2cap.
```
python3 run.py --config config/eval/{task}_config.yml
```

### Acknowledgement
We would like to thank the authors of [Vil3dref](https://github.com/cshizhe/vil3dref), [3D-Vista](https://github.com/3d-vista/3D-VisTA), [3D-VLP](https://github.com/leolyj/3D-VLP/tree/main) and for their open-source release.



### Citation:

```
@inproceedings{3DSyn,
  title     = {3D Vision and Language Pretraining with Large-Scale Synthetic Data},
  author    = {Dejie Yang, Zhu Xu, Wentao Mo, Qingchao Chen, Siyuan Huang, Yang Liu},
  booktitle = {Proceedings of the Thirty-Second International Joint Conference on
               Artificial Intelligence, {IJCAI-24}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  year      = {2024},
}

```
