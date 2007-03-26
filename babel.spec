Summary:	Program to interconvert a number of file formats currently used in molecular modeling.
Summary(pl.UTF-8):	Program do konwersji między wieloma formatami plików używanych w kodelowaniu molekularnym.
Name:		babel
Version:	1.6
Release:	1
License:	as-is
Group:		Libraries
Source0:	http://smog.com/chem/babel/files/%{name}-%{version}.tar.Z
# Source0-md5:	101a5dc4858ecacac123571db52b272e
Patch0:		%{name}-gcc3.patch
URL:		http://smog.com/chem/babel/
BuildRequires:	rpmbuild(macros) >= 1.316
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	program_name	babel1

%description
Babel is a program designed to interconvert a number of file formats
currently used in molecular modeling.  Babel is capable of assigning
hybridization, bond order, and connectivity when these elements are
not present in the input file.

Babel is not developed, but still provides some formats not supported
yet by new OpenBabel.

%description -l pl.UTF-8
Babel jest programem służącym do konwersji między wieloma formatami
plików używanych w modelowaniu molekularnym.  Babel umie określać
hybrydyzację, rząd wiązania i połączenia brakujące w pliku wejściowym.

Babel nie jest rozwijany, jednak nadal obsługuje niektóre formaty
nieobsługiwane przez nowy program OpenBabel.

%prep
%setup -q
%patch0

%build
%{__make} \
    CC='%{__cc}' \
    CFLAGS='%{rpmcflags}' \
    LDFLAGS='%{rpmldflags}' \
    PROGRAM='%{program_name}'

%install
rm -rf $RPM_BUILD_ROOT
install -d \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_datadir}/%{name} \
    $RPM_BUILD_ROOT/etc/env.d

%{__make} install \
    DEST=$RPM_BUILD_ROOT%{_bindir} \
    PROGRAM='%{program_name}'

install *.lis $RPM_BUILD_ROOT%{_datadir}/%{name}
echo BABEL_DIR=%{_datadir}/%{name} > $RPM_BUILD_ROOT/etc/env.d/BABEL_DIR

%clean
rm -rf $RPM_BUILD_ROOT

%post
%env_update

%postun
%env_update

%files
%defattr(644,root,root,755)
%doc README.1ST
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/env.d/*
