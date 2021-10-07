import React from 'react';

// article loading component for displaying the wating message untile fetchArticle function of app component do not return any data
const ArticleLoading = () => {
    return (
        <div>
            <p style={{textAlign:"center", marginTop:"1rem" ,fontSize: '25px'}}>
                We are waiting for the data to load !...
            </p>
        </div>
    )
}

export default ArticleLoading;
