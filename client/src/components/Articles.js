import React from 'react'
// third party imports of material ui
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
// local import 
import ArticleLoading from './ArticleLoading';

// articles component for displaying all the articles which are fetched from blog api
const Articles = ({articles}) => {
    // if there is no article the return the ArticleLoading component
    if(articles.length === 0){
        return(
            <section style={{minHeight:"calc(100vh - 70px)"}}>
                <ArticleLoading/>
            </section>
        )
    }
    // returning jsx if there is any article available
    return (
        <section style={{minHeight:"calc(100vh - 70px)"}}>
            <Box sx={{ flexGrow: 1 }}>
                <Grid container margin="auto"  sx={{ maxWidth: "85vw"}} spacing={2}> 
                {/* grid container starts here */}
                    {/* map over articles array props to display each article */}
                    {articles.map((article, index) =>{
                    return(
                        <Grid item xs={12} md={3} key={index}>
                            <Card sx={{ maxWidth: 345 }}>
                                <CardMedia
                                    component="img"
                                    alt="green iguana"
                                    height="140"
                                    // using picsum api for image source
                                    image={`https://picsum.photos/id/${article.id}/200/300`}
                                />
                                <CardContent>
                                    <Typography gutterBottom variant="h6" component="div">
                                    {article.title}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                    {article.description}
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small">Share</Button>
                                    <Button size="small">See More</Button>
                                </CardActions>
                            </Card>
                        </Grid>
                        )
                    })}
                {/* grid container ends here */}
                </Grid>
            </Box>
        </section>
    )
}

// exporting articles component so that it can be accessible by app components
export default Articles;
