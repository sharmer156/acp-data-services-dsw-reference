FROM adobe/acp-dsw-ml-runtime-r:0.2.1

WORKDIR /root/sample/code

COPY . .

# Install Additional Packages
RUN install2.r gbm
RUN install2.r lubridate
RUN install2.r tidyverse

RUN R -e 'library(devtools);document()'
RUN R --no-site-file --no-environ --no-save --no-restore --quiet CMD build . --no-resave-data

RUN cp *.tar.gz /root/runtime/ml.retail.r.tar.gz

RUN rm -rf /root/sample/code


WORKDIR /root/runtime

RUN install2.r -l /root/sample  ml.retail.r.tar.gz
