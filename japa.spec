#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	JACK and ALSA Perceptual Analyser
Name:		japa
Version:	0.8.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	966a8774e5b232bf055922dfdcc1b730
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/index.html
BuildRequires:	clthreads-devel
BuildRequires:	clxclient-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	zita-alsa-pcmi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japa (JACK and ALSA Perceptual Analyser), is a 'perceptual' or
'psychoacoustic' audio spectrum analyser. In contrast to JAAA, this is
more an acoustical or musical tool than a purely technical one.
Possible uses include spectrum monitoring while mixing or mastering,
evaluation of ambient noise, and (using pink noise), equalisation of
PA systems.

%prep
%setup -q
%patch0 -p1

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
