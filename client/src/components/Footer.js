import React from 'react'
// third party import of material ui
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import Container from '@mui/material/Container';
// makeStyle api import of material ui
import { makeStyles } from '@mui/styles';

// creating useStyles component using makeStyles api for styling of copyright class.
const useStyles = makeStyles(() => ({
    copyright:{
        color:"text.secondary",
        align:"center",
    }
}));

// Copyright component of footer section
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


// data related to footer compoent in the array of objects format
const footers = [
  // first column data of footer
    {
      title: 'Company',
      description: ['Team', 'History', 'Contact us', 'Locations'],
    },
  // second column data of footer
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
  // third column data of footer
    {
      title: 'Resources',
      description: ['Resource', 'Resource name', 'Another resource', 'Final resource'],
    },
  // fourth column data of footer
    {
      title: 'Legal',
      description: ['Privacy policy', 'Terms of use'],
    },
  ];

// footer component for displaying footer
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
                  {/* iterating over footers array variable using map  */}
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
                {/* adding copyright component at the bottom of footer */}
                <Copyright sx={{ mt: 5 }} />
            </Container>
            {/* End footer */}
        </>
    )
}

// exporting footer so that it will be accessible in index file
export default Footer;
