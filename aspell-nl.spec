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
Release:	24
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-nl
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
./configure
%make

%install
%makeinstall_std

# fix doc perms
chmod 644 README doc/*

cd %{buildroot}%{_libdir}/aspell && ln -s nl.rws nederlands

%files
%doc README 
%{_libdir}/aspell-%{aspell_ver}/*

