import React, { useState } from 'react';
import { uploadArtwork } from '../services/api';

const UploadArtwork = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [fileUrl, setFileUrl] = useState('');
    const [price, setPrice] = useState('');

    const handleUpload = () => {
        const artwork = { title, description, file_url: fileUrl, price: parseFloat(price) };
        uploadArtwork(artwork).then(() => alert('Artwork uploaded!'));
    };

    return (
        <div className="upload-artwork">
            <h2>Upload Your Artwork</h2>
            <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
            <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" />
            <input value={fileUrl} onChange={(e) => setFileUrl(e.target.value)} placeholder="File URL" />
            <input value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" type="number" />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default UploadArtwork;
