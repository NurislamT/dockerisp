FROM python:3.7
MAINTAINER nurislam
WORKDIR example
RUN apt-get update && apt-get install -y texlive
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install seaborn
ADD code ./code
ADD data ./data
ADD latex ./latex
ADD run.sh ./
RUN chmod +x run.sh
VOLUME /example/results
CMD ./run.sh

