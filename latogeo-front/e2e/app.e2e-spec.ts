import { LatogeoFrontPage } from './app.po';

describe('latogeo-front App', () => {
  let page: LatogeoFrontPage;

  beforeEach(() => {
    page = new LatogeoFrontPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
