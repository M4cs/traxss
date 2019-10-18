FROM xshuden/alppython3
MAINTAINER Furkan SAYIM | furkan.sayim@yandex.com

RUN git clone https://github.com/xShuden/traxss.git /tmp/traxss

WORKDIR /tmp/traxss

RUN pip3 install -r requirements.txt

CMD ["python3", "traxss.py"]