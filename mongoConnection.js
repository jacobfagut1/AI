// Import MongoClient and ServerApiVersion from the 'mongodb' package
const { MongoClient, ServerApiVersion } = require('mongodb');

// Define your MongoDB Atlas connection URI (replace <db_password> with your actual password)
const uri = "mongodb+srv://mjefagut01:secretpassword@cluster0.9lahgmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

// Create a MongoClient instance with options to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

// Function to run the connection and perform the ping test
async function run() {
  try {
    // Connect the client to the MongoDB server
    await client.connect();
    
    // Send a ping to confirm the connection was successful
    await client.db("admin").command({ ping: 1 });
    
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } catch (error) {
    console.error("Error connecting to MongoDB:", error);
  } finally {
    // Ensure that the client closes after the operation is finished
    await client.close();
  }
}

// Call the run function
run().catch(console.dir);
