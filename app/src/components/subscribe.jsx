import '../styles.css';
import { useState } from 'react';

const Subscribe = () => {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('http://localhost:5000/api/recieve_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });
        const jsonData = await response.json();
        if (response.ok) {
            setEmail('');
            setMessage(jsonData['message']);
        } else {
            setMessage('Failed to submit email.');
        }
    };

    return (
        <div className='subscribe-around'>
            <div className="subscribe">
                <h2>Subscribe for Announcements</h2>
                <form onSubmit={handleSubmit}>
                    <input
                        type="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                    <input type="submit" value="Submit" />
                </form>
                {message && <p>{message}</p>}
            </div>
        </div>
    );
};

export default Subscribe;
