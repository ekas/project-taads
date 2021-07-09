FROM node:12-alpine
COPY . .
RUN apk update && apk upgrade
RUN apk add git
RUN yarn install
RUN yarn run build
# expose 5000 on container
EXPOSE 3000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=3000

# start the app
CMD [ "yarn", "start" ]