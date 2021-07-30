%global srcname sphinx-copybutton

Name:           python-%{srcname}
Version:        0.3.1
Release:        %mkrel 1
Summary:        Add a copy button to code cells in Sphinx docs
Group:          Development/Python
License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  ipython
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.

%package -n     python3-%{srcname}
Summary:        Add a copy button to code cells in Sphinx docs
Group:          Development/Python
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.

%package        doc
Summary:        Documentation for %{srcname}

%description    doc
Documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf sphinx_copybutton.egg-info

%build
%py3_build

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/_build/html/.buildinfo

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/sphinx_copybutton*

%files doc
%doc doc/_build/html
%license LICENSE
