import React, { useEffect, useState } from 'react';
import { fetchArtworks } from '../services/api';

const Gallery = () => {
    const [artworks, setArtworks] = useState([]);

    useEffect(() => {
        fetchArtworks().then(data => setArtworks(data));
    }, []);

    return (
        <div className="gallery">
            {artworks.map(artwork => (
                <div key={artwork.id}>
                    <img src={artwork.file_url} alt={artwork.title} />
                    <h3>{artwork.title}</h3>
                    <p>{artwork.description}</p>
                </div>
            ))}
        </div>
    );
};

export default Gallery;
