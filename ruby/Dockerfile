FROM ruby:3-alpine3.13

WORKDIR /app
COPY . .
RUN gem install bundler
RUN bundle install
