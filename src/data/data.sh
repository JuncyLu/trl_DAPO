# python src/data/dataset_aokvqa.py \
#   --splits train \
#   --out_dir ./dataset/aokvqa_openr1 \
#   --question_id_file /home/lujunxi57/trl/A-OKVQA_question_id.txt

# python src/data/dataset_visrag_arxivqa.py \
#   --out_dir ./dataset/visrag_arxivqa_openr1 \
#   --split train

# python src/data/dataset_mmmupro.py \
#   --subset "standard (4 options)" \
#   --out_dir ./dataset/mmmu_pro_4opt_openr1

python src/data/merge_parquet.py \
  --inputs ./data/aokvqa_openr1/train/train-00000-of-00001.parquet \
           ./data/visrag_arxivqa_openr1/train/train-00000-of-00001.parquet \
           ./data/mmmu_pro_4opt_openr1/train/standard_4_options_test-00000-of-00001.parquet \
  --output ./DDM/train/train-00000-of-00001.parquet