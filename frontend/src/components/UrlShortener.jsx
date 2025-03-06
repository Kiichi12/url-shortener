import React, { useState } from 'react';
import axios from 'axios';



const UrlShortener = () => {
    const [url, setUrl] = useState('');
    const [shortUrl, setShortUrl] = useState('');
    
    const BACKEND_URL = "https://url-shortener-7kd0.onrender.com/";

    const handleShorten = async () => {
        try {
            const response = await axios.post(`${BACKEND_URL}/api/url/shorten`, { url });
            setShortUrl(response.data.short_url);
        } catch (error) {
            alert('Failed to shorten URL');
        }
    };
    // const handleShorten = async () => {
    //     try {
    //         const response = await axios.post('http://localhost:5000/api/url/shorten', { url });
    //         setShortUrl(response.data.short_url);
    //     } catch (error) {
    //         alert('Failed to shorten URL');
    //     }
    // };

    return (
        <div>
            <h2>URL Shortener</h2>
            <input type="text" placeholder="Enter URL" value={url} onChange={(e) => setUrl(e.target.value)} />
            <button onClick={handleShorten}>Shorten</button>
            {shortUrl && <input type="text" value={shortUrl} readOnly />}
        </div>
    );
};

export default UrlShortener;
