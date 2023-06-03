FROM node:18

RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

COPY .env ./.env

RUN chmod +x ./.env

RUN pip3 install -r requirements.txt

RUN mkdir -p uploads

RUN npm run build

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

USER nextjs

EXPOSE 3000
EXPOSE 8000

ENV PORT 3000

CMD ["npm", "run", "start"]