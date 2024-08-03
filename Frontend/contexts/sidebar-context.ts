import { createContext } from 'react';

interface SidebarContextValue {
  sidebarStatus: boolean;
  toggleSidebar: () => void;
}

const sidebarContext = createContext<SidebarContextValue | false>(false);

export default sidebarContext;