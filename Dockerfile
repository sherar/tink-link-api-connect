FROM python:3.9-alpine

WORKDIR /usr/src/app

RUN apk add py-pip make
COPY . .
RUN make init

# Add a new user "john" with user id 8877
RUN addgroup -S demousers && adduser -S john -G demousers
# Change to non-root privilege
USER john

CMD ["make", "run"]