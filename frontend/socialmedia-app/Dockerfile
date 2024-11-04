# Use the official Node.js image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the React project files
COPY . .

# Expose the port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
