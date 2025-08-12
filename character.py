from typing import Optional

class Character:
    def __init__(self, id, name, korean_name, description, normal_image_path=None, blush_image_path=None, affection=30):
        self.id = id
        self.name = name
        self.korean_name = korean_name
        self.description = description
        self.normal_image_path = normal_image_path
        self.blush_image_path = blush_image_path
        self.affection = affection

        
        # 강재호는 이미지가 없음
        if self.id == "KANG":
            self.normal_image_path = None
            self.blush_image_path = None
            self.affection = 0 