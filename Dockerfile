FROM python

#creating directory helloworld in container (linux machine)
RUN pip install pytest && pip install selenium
RUN mkdir \Users\aaa\selenium 

#copying helloworld.py from local directory to container's helloworld folder

COPY . /app/user 
WORKDIR /app/user/tests/  

RUN command ls
RUN pwd

RUN  cd /app/user/tests/

# RUN ls
#running helloworld.py in container

CMD pytest -v

# ENTRYPOINT ["pytest" ]