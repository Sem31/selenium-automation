FROM python


RUN pip install pytest && pip install selenium && pip install pytest-html && pip install requests && pip install pytest-rerunfailures
RUN mkdir \Users\sdosi\selenium

COPY . /app/user
WORKDIR /app/user/cms-ui-automation/test/


VOLUME /app/user/tests/myvolume
CMD ENV_NAME='uplynk' pytest -vs -m regression --disable-warnings -W ignore::DeprecationWarning --html=../../../../data/report.html --reruns 4
