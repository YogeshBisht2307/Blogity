import React from 'react'
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import ArticleLoading from './ArticleLoading';

const Articles = ({articles}) => {
    if(articles.length === 0){
        return(
            <section style={{minHeight:"calc(100vh - 70px)"}}>
                <ArticleLoading/>
            </section>
        )
    }
    return (
        <section style={{minHeight:"calc(100vh - 70px)"}}>
            <Box sx={{ flexGrow: 1 }}>
                <Grid container margin="auto"  sx={{ maxWidth: "85vw"}} spacing={2}> 
                {/* grid container starts here */}
                    {articles.map((article, index) =>{
                    return(
                        <Grid item xs={12} md={3} key={index}>
                            <Card sx={{ maxWidth: 345 }}>
                                <CardMedia
                                    component="img"
                                    alt="green iguana"
                                    height="140"
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
                                    <Button size="small">Learn More</Button>
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

export default Articles
