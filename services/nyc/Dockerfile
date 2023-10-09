FROM ruby:2.3.1

ENV APPLICATION_ROOT /app/

RUN gem install sinatra:1.4.7 json:2.6.3 puma:3.12.6

WORKDIR $APPLICATION_ROOT
ADD . $APPLICATION_ROOT

EXPOSE 9292

ENTRYPOINT ["puma", "-e", "production"]
