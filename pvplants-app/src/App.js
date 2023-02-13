import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Layout, Menu, Popover } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  AppstoreOutlined,
  FileOutlined,
  SettingOutlined,
  UserOutlined,
  LogoutOutlined,
} from '@ant-design/icons';
import Dashboard from './Dashboard';
import PlantDetails from './PlantDetails';
import MaintenanceLogs from './MaintenanceLogs';

const { Header, Sider, Content } = Layout;

function App() {
  const [collapsed, setCollapsed] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);

  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };

  const handleLogout = () => {
    setLoggedIn(false);
  };

  const userMenu = (
    <Menu>
      {loggedIn ? (
        <Menu.Item key="logout" onClick={handleLogout} icon={<LogoutOutlined />}>
          Logout
        </Menu.Item>
      ) : (
        <Menu.Item key="login" icon={<UserOutlined />}>
          <Link to="/login">Login</Link>
        </Menu.Item>
      )}
    </Menu>
  );

  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        <Sider trigger={null} collapsible collapsed={collapsed}>
          <div className="logo" style={{ height: '32px', margin: '16px' }}>
          <div style={{ fontSize: '18px', fontWeight: 'bold', color: 'white' }}>Micro Electricity</div>
          </div>
          
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1" icon={<AppstoreOutlined />}>
              <Link to="/">Dashboard</Link>
            </Menu.Item>
            <Menu.Item key="2" icon={<FileOutlined />}>
              <Link to="/plants">Plants</Link>
            </Menu.Item>
            <Menu.Item key="3" icon={<SettingOutlined />}>
              <Link to="/maintenance">Maintenance Logs</Link>
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout className="site-layout">
          <Header className="site-layout-background" style={{ padding: 0 }}>
            {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
              className: 'trigger',
              onClick: toggleCollapsed,
            })}
      </Header>
      <Content style={{ margin: '24px 16px', padding: 24, minHeight: 280 }}>
        <Routes>
          <Route exact path="/" element={<Dashboard />} />
          <Route exact path="/plants" element={<PlantDetails />} />
          <Route exact path="/maintenance" element={<MaintenanceLogs />} />
        </Routes>
      </Content>
    </Layout>
  </Layout>
</Router>
);
}

export default App;
