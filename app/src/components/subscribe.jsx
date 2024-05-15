import '../styles.css';

const Subscribe = () => {
    return (
        <div className="subscribe">
            <h2>Subscribe for Announcements</h2>
            <form action="#">
                <input type="email" placeholder="Email" required />
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
};

export default Subscribe;