const fs = require('fs');
const path = require('path');
const https = require('https');

const menuImages = {
  'salmon.jpg': 'https://img.freepik.com/free-photo/grilled-salmon-fish-with-spinach-salad_140725-3664.jpg',
  'beef.jpg': 'https://img.freepik.com/free-photo/grilled-beef-steak-with-vegetables_140725-2000.jpg',
  'risotto.jpg': 'https://img.freepik.com/free-photo/creamy-mushroom-risotto-with-parmesan-cheese_140725-2000.jpg',
  'bruschetta.jpg': 'https://img.freepik.com/free-photo/bruschetta-with-tomatoes-basil_140725-2000.jpg',
  'caesar.jpg': 'https://img.freepik.com/free-photo/caesar-salad-with-chicken-parmesan-cheese-croutons_140725-2000.jpg',
  'tiramisu.jpg': 'https://img.freepik.com/free-photo/tiramisu-cake-with-cocoa-powder_140725-2000.jpg',
  'cheesecake.jpg': 'https://img.freepik.com/free-photo/new-york-cheesecake-with-berries_140725-2000.jpg',
  'soup.jpg': 'https://img.freepik.com/free-photo/minestrone-soup-with-vegetables_140725-2000.jpg',
  'alfredo.jpg': 'https://img.freepik.com/free-photo/chicken-alfredo-pasta-with-creamy-sauce_140725-2000.jpg',
  'lasagna.jpg': 'https://img.freepik.com/free-photo/vegetable-lasagna-with-tomato-sauce_140725-2000.jpg',
  'garlic-bread.jpg': 'https://img.freepik.com/free-photo/garlic-bread-with-herbs_140725-2000.jpg'
};

const menuDir = path.join(__dirname, '../../public/images/menu');

// Create menu directory if it doesn't exist
if (!fs.existsSync(menuDir)) {
  fs.mkdirSync(menuDir, { recursive: true });
}

// Download each image
Object.entries(menuImages).forEach(([filename, url]) => {
  const filePath = path.join(menuDir, filename);
  
  // Skip if file already exists
  if (fs.existsSync(filePath)) {
    console.log(`${filename} already exists, skipping...`);
    return;
  }
  
  https.get(url, (response) => {
    if (response.statusCode === 200) {
      const fileStream = fs.createWriteStream(filePath);
      response.pipe(fileStream);
      
      fileStream.on('finish', () => {
        fileStream.close();
        console.log(`Downloaded ${filename}`);
      });
    } else {
      console.error(`Failed to download ${filename}: ${response.statusCode}`);
    }
  }).on('error', (err) => {
    console.error(`Error downloading ${filename}:`, err.message);
  });
}); 