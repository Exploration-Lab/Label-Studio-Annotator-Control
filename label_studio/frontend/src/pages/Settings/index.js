import React from 'react';
import { SidebarMenu } from '../../components/SidebarMenu/SidebarMenu';
import { GeneralSettings } from './GeneralSettings';



export const MenuLayout = ({children, ...routeProps}) => {
  return (
    <SidebarMenu
      menuItems={[
   
      ]}
      path={routeProps.match.url}
      children={children}
    />
  );
};
// Have removed the Danger Zone, Cloud Storage & WebHooks menuItems

export const SettingsPage = {
  title: "Settings",
  path: "/settings",
  exact: true,
  layout: MenuLayout,
//   component: GeneralSettings,
  pages: {
    
  },
};
// Have removed the Danger Zone, Cloud Storage & WebHooks Pages from Settings