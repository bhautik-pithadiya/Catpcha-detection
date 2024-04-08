from captcha.src.captcha.image import ImageCaptcha
import random
import string
import typing as t
ColorTuple = t.Union[t.Tuple[int, int, int], t.Tuple[int, int, int, int]]



def main():
    image = ImageCaptcha(
        width = 200,
        height = 100,
        
        # fonts=[
        #     'captcha/src/captcha/data/Noto_Sans/NotoSans-VariableFont_wdth,wght.ttf',
        # 'captcha/src/captcha/data/Fira_Sans,Noto_Sans/Fira_Sans/FiraSans-Light.ttf'
        #     ]
        )



    txt = 'Hello1'
    image._difficulty = 'hard'
    captcha_image = image.generate(txt)
    image_file = "./temp.png"
    image.write(txt, image_file)

if __name__ == '__main__':
    main()