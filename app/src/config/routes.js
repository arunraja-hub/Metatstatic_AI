import React from 'react';
import Loadable from 'react-loadable';

import Home from '../containers/Home';

function Loading() {
  return <div>Loading...</div>;
}

const Dashboard = Loadable({
  loader: () => import('../containers/views/Dashboard'),
  loading: Loading,
});

const ImageAnalysis = Loadable({
  loader: () => import('../containers/views/ImageAnalysis'),
  loading: Loading,
});

const Page1 = Loadable({
  loader: () => import('../containers/views/Page1'),
  loading: Loading,
});

const Page2 = Loadable({
  loader: () => import('../containers/views/ImageAnalysis'),
  loading: Loading,
});

const ImageGallery = Loadable({
  loader: () => import('../containers/views/ImageAnalysis'),
  loading: Loading,
});

const routes = [
  { path: '/', name: '', component: Home, exact: true },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/ImageAnalysis', name: 'Image Analysis', component: ImageAnalysis },
  { path: '/ImageGallery', name: 'Image Analysis', component: ImageGallery },
  { path: '/page1', name: 'Page1', component: Page1 },
  { path: '/page2', name: 'Page2', component: Page2 }
];

export default routes;
