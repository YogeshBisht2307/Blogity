import React, {useState, useEffect} from 'react';
import Articles from './components/Articles';

// app Component
const App = () => {
    // useState hook for handling the state of article
    const [articles, setArticles] = useState([]);
    // useEffect hook for calling the api after rendering of application
    useEffect(() =>{
        // defining fetchArticles function,fetchArticles is set to be async function because it going to return the promises
        const fetchArticles = async() =>{
            try{
                // hitting the api url and waiting for data to be fetched from the api
                const response = await fetch('http://localhost:8000/api/');
                // converting response data into json format
                const articles = await response.json();
                // updating the state of article using setArticle function
                setArticles(articles);
            }catch(error){
                console.error(error);
            }
        }
    // calling the fetchArticles function
    fetchArticles();
    }, []);

    // returning the jsx
    return (
        <div className="App">
            <h1 style={{textAlign:"center", marginTop:"1rem"}}>Latest Post</h1>
            {/* adding the articles component and passing articles state as props  */}
            <Articles articles={articles}/>
        </div>
    )
}

// exporting app component so that it can be accessible by other components
export default App;
