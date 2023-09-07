Установка на ubuntu22 ->

Можно установить на семействах Debian
скопируйте команды шаг за шагом

1) sudo apt install -y git
2) git clone https://github.com/ZhangaliMalikazhdar/pdf-to-txt.git
3) cd pdf-to-txt
4) . installation.sh

в папке pdfs пдф переименовал как '1.pdf' и рядом генерируется 'page.jpg'
можно удалить page.jpg
также можно в вручную запустить команду 'python run.py'
а если хотите другой пдф скинуть, то также в pdfs/ кидаете и запускаете через 'python run_with_input_file.py [имя пдфа]'
виртуальное окружение в папке 'v/'
