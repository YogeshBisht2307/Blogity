import React, {useState, useEffect} from 'react';
import Articles from './components/Articles';



const App = () => {
    const [articles, setArticles] = useState([]);
    useEffect(() =>{
        const fetchArticles = async() =>{
            try{
                const response = await fetch('http://localhost:8000/api/');
                const articles = await response.json();
                setArticles(articles);
            }catch(error){
                console.error(error);
            }
        }
    fetchArticles();
    }, []);
    return (
        <div className="App">
            <h1 style={{textAlign:"center", marginTop:"1rem"}}>Latest Post</h1>
            <Articles articles={articles}/>
        </div>
    )
}

export default App
