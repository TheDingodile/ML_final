import json
from PIL import Image
import inference
from inference.models.paligemma.paligemma import PaliGemma


def run_test(root_path: str):
    key = "fbbZZyxhAw17JHCvAIrZ"
    pg = PaliGemma(api_key=key)

    images_path = "resized_ratio_short_side_768"
    questions_path = "mimic-cxr-vqa/train.json"

    # open question_path
    with open(root_path + "/" + questions_path, 'r') as f:
        questions = json.load(f)

    for question in questions:
        image_id = question['image_id']
        question_text = question['question']
        answer = question['answer']
        print(question_text)
        print(answer)

        image = Image.open(root_path + "/" + images_path + "/" + image_id + ".jpg")
        image = image.convert('RGB')
        result = pg.predict(image, question_text)
        print(result)