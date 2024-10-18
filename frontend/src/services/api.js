import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const fetchArtworks = async () => {
    const response = await axios.get(`${API_URL}/artworks/`);
    return response.data;
};

export const uploadArtwork = async (data) => {
    const response = await axios.post(`${API_URL}/artwork/`, data);
    return response.data;
};
