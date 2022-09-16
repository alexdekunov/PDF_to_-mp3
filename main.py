from gtts import gTTS
import pdfplumber

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path) == '.pdf':
        return 'File exists!'
    else:
        return 'File not exist, check the file path'

def Pdf_to_mp3():
    print(pdf_to_mp3(file_path='\Dekunov\Documents\HYPER\HIPER_CORP_v5_3_сент.pdf'))

if __name__ == '__Pdf_to_mp3__':
    main()