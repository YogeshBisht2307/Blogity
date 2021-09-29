import React from 'react'
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import Container from '@mui/material/Container';
import { makeStyles } from '@mui/styles';


const useStyles = makeStyles(() => ({
    copyright:{
        color:"text.secondary",
        align:"center",
    }
}));


const Copyright = (props) => {
    const classes = useStyles();
    return (
      <Typography variant="body2" className={classes.copyright} {...props}>
        {'Copyright © '}
        <Link style={{color:"inherit"}} href="#">
          Your Website
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }



const footers = [
    {
      title: 'Company',
      description: ['Team', 'History', 'Contact us', 'Locations'],
    },
    {
      title: 'Features',
      description: [
        'Cool stuff',
        'Random feature',
        'Team feature',
        'Developer stuff',
        'Another one',
      ],
    },
    {
      title: 'Resources',
      description: ['Resource', 'Resource name', 'Another resource', 'Final resource'],
    },
    {
      title: 'Legal',
      description: ['Privacy policy', 'Terms of use'],
    },
  ];


const Footer = () => {
    return (
        <>
            {/* Footer */}
            <Container
                maxWidth="md"
                component="footer"
                sx={{
                borderTop: (theme) => `1px solid ${theme.palette.divider}`,
                mt: 8,
                py: [3, 6],
                }}
            >
                <Grid container spacing={4} justifyContent="space-evenly">
                {footers.map((footer) => (
                    <Grid item xs={6} sm={3} key={footer.title}>
                    <Typography variant="h6" style={{color:"text.primary"}} gutterBottom>
                        {footer.title}
                    </Typography>
                    <ul>
                        {footer.description.map((item) => (
                        <li key={item}>
                            <Link href="#" variant = "subtitle1" style = {{color:"text.secondary"}}>
                            {item}
                            </Link>
                        </li>
                        ))}
                    </ul>
                    </Grid>
                ))}
                </Grid>
                <Copyright sx={{ mt: 5 }} />
            </Container>
            {/* End footer */}
        </>
    )
}

export default Footer
