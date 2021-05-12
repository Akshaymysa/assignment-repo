FROM python
RUN pip3 install flask pyyaml requests
COPY main.py /
CMD [ "python3", "main.py" ]
