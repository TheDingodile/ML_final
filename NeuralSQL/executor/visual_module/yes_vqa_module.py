from .vqa_module import VQAModule


class YesVQAModule(VQAModule):
    def __init__(self):
        pass

    def load_model(self):
        # No need to load any model
        pass

    def preprocess_input(self, images, questions):
        # No preprocessing required
        return images, questions

    def postprocess_output(self, raw_output):
        handled_answers = []
        for answer in raw_output:
            if not answer:
                # Handles empty answer case
                handled_answers.append(None)  # Using None to represent no answer
            elif isinstance(answer, list):
                # Handles list of answers
                if all(a.lower() in ["yes", "no"] for a in answer):
                    handled_answers.append([a.lower() == "yes" for a in answer])
                else:
                    handled_answers.append(answer)
            elif answer.lower() in ["yes", "no"]:
                # Handles single answers
                handled_answers.append(answer.lower() == "yes")
            else:
                handled_answers.append(answer)  # Handles non-yes/no answers

        return handled_answers

    def __call__(self, images, questions):
        # if len(preprocessed_questions) > 1:
        #     return "null"
        # Preprocess the input images and questions (no-op)
        preprocessed_images, preprocessed_questions = self.preprocess_input(images, questions)
        # print(len(preprocessed_questions))

        # Simulate obtaining a raw_output list that is always "yes" for each question
        # print(preprocessed_images, preprocessed_questions)
        # print(" ")
        raw_output = ["yes"] * len(preprocessed_questions)  # Generate a "yes" for each question
        answer_probs = [0.5] * len(preprocessed_questions)  # Generate a probability of 0.5 for each question
        # print(questions)
        # print(images)
        # print(len(preprocessed_questions))
        # print(preprocessed_questions)
        # Postprocess the output to obtain the handled answers
        handled_answers = self.postprocess_output(raw_output)
        # answer_probs = self.postprocess_output(answer_probs)

        # print(raw_output, handled_answers, answer_probs)
        # check that all answers are either "yes" or "no"
        if not all(isinstance(answer, bool) for answer in handled_answers):
            return "null"
        
        product = 1
        for number in answer_probs:
            product *= number

        if product < 0.5:
            return "null"
        return handled_answers
