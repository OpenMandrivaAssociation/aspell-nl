%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-2
%define fname aspell-%{languagecode}
%define aspell_ver 0.60
%define languagelocal nederlandse
%define languageeng dutch
%define languageenglazy Dutch
%define languagecode nl
%define lc_ctype ln_NL

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.2
Release:	%mkrel 18
Group:		System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-nl

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary

# RedHat Stuff. is this right:
#Obsoletes: ispell-fr, ispell-french

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
./configure
%make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# fix doc perms
chmod 644 README doc/*

cd $RPM_BUILD_ROOT%{_libdir}/aspell && ln -s nl.rws nederlands

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{_libdir}/aspell-%{aspell_ver}/*


