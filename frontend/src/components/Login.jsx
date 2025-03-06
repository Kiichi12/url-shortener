import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const BACKEND_URL = "https://url-shortener-7kd0.onrender.com";

    const handleLogin = async () => {
        try {
            const response = await axios.post(`${BACKEND_URL}/api/url/shorten`, { url });
            if (response.status === 200) {
                navigate('/url-shortener');
            }
        } catch (error) {
            alert('Invalid credentials');
        }
    };

    return (
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px' }}>
            <h2>Login</h2>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
            <p>Don't have an account? <a href="/register">Register</a></p>
        </div>
    );
};

export default Login;
