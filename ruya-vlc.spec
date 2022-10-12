Name: ruya-vlc
Version: 1
Release: 1%{?dist}
Summary: VLC Customization for Ruya 
License: GPLv3
URL: https://parmg.sa
Source0: LICENSE
Source1: vlcrc
BuildArch: noarch

%description
VLC Customization for Ruya

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/vlc
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.config/vlc

%files
%license LICENSE
%{_sysconfdir}/skel/.config/vlc/vlcrc

%changelog
* Tue Oct 11 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1-1
- Initial
