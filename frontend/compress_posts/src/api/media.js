import axios from 'axios';

const API = "http://localhost:8000/api/media";

// Step 1 -> get presigned URL
export const getPresignedURL = async (file) => {
  try {
    const res = await axios.post(`${API}/generate-upload-url/`, {
      filename: file.name,
      content_type: file.type,
    });
    return res.data;
  } catch (err) {
    console.error("Presigned URL error:", err.response?.data);
    throw err;
  }
};

// Step 2 -> upload file to s3
export const uploadToS3 = async (uploadUrl, file) =>{
    await axios.put(uploadUrl, file,{
        headers:{
            "Content-Type": file.type,
        },
    });
};

// Step 3 → Tell Django to create MediaFile
export const saveMediaRecord = async (raw_key, filename) => {
  const res = await axios.post(`${API}/files/create/`, {
    raw_s3_key: raw_key,
    original_filename: filename,
  });
  return res.data;
};

// Fetch Posts
export const getPosts = async () => {
  const res = await axios.get(`${API}/files/`);
  return res.data; // Contains file_url (compressed URL)
};
