FROM python

#creating directory helloworld in container (linux machine)
RUN pip install pytest && pip install selenium && pip install pytest-html
RUN mkdir \Users\aaa\selenium 

#copying helloworld.py from local directory to container's helloworld folder

COPY . /app/user 
WORKDIR /app/user/tests/  

RUN command ls
RUN pwd

RUN  cd /app/user/tests/

# VOLUME /app/user/tests/myvolume
CMD pytest --html=../../../data/report.html                       

#  docker run -v $(pwd)/kp:/data kp1