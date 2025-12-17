%global srcname sphinx-copybutton

Name:           python-%{srcname}
Version:        0.5.2
Release:        1
Summary:        Add a copy button to code cells in Sphinx docs
Group:          Development/Python
License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:	https://files.pythonhosted.org/packages/fc/2b/a964715e7f5295f77509e59309959f4125122d648f86b4fe7d70ca1d882c/sphinx-copybutton-%{version}.tar.gz
#Source0:        https://files.pythonhosted.org/packages/source/sphinx-copybutton/sphinx-copybutton-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  ipython
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.

%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf sphinx_copybutton.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE
%{python_sitelib}/sphinx_copybutton*

