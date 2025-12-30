# Created by pyp2rpm-3.3.3
%bcond_without tests
%global pypi_name hsaudiotag3k

Name:           python-%{pypi_name}
Version:        1.1.3.post1
Release:        5
Summary:        Python library for reading audo tags

License:        BSD
URL:            https://github.com/irmen/Serpent
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
hsaudiotag is a pure Python library that lets you read metadata (bitrate, sample rate, duration
and tags) from mp3, mp4, wma, ogg, flac and aiff files. It can only read tags, not write to them

%{?python_provide:%python_provide python-%{pypi_name}}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
#%%license LICENSE
%doc README.rst CHANGES
%{python3_sitelib}/*

# %{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

