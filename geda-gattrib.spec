Summary:	Gattrib for gEDA project
Summary(pl):	Gattrib dla projektu gEDA
Name:		geda-gattrib
Version:	20061020
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	74295c8b0b0d78ebf0953673ecdfb28f
URL:		http://www.geda.seul.org/
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gattrib for the gEDA project.

%description -l pl
Gattrib dla projektu gEDA.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc AUTHORS ChangeLog* NEWS README docs/README.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-gattribrc
